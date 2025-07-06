from django.db import models

# Create your models here.
from django.db import models

class HomePageContent(models.Model):
    """Model to store content for the home page."""
    name = models.CharField(max_length=25, default='Sivaguru M', help_text='Enter Your Name')
    roles = models.TextField(help_text="Comma-separated roles, e.g., 'Full-stack Developer, Python Developer'", default="Full-stack Developer, Python Developer")
    introduction_text = models.TextField(default="Welcome to my portfolio! I'm a self-taught web developer passionate about building and deploying real-world web applications. I specialize in full-stack projects with a focus on robust backend logic and clean user interfaces, often incorporating user authentication. I'm eager to contribute my skills to meaningful projects and continue growing as a developer.")
    cv_pdf = models.FileField(upload_to='assets/', blank=True, null=True, help_text="Upload your CV PDF")

    def get_roles_list(self):
        return [role.strip() for role in self.roles.split(',')]

    def __str__(self):
        return "Home Page Content"
    
class AboutPageContent(models.Model):
    """Model to store content for the about page."""
    initial_paragraph = models.TextField(default="I’m a self-taught web developer passionate about building and deploying real-world web applications. I specialize in full-stack development with a strong focus on backend logic and clean, user-friendly interfaces. I often work on projects that include user authentication and dynamic features.")
    read_more_paragraph = models.TextField(help_text="Content for the 'Read More' section.", default="I am focused on improving my skills every day by learning new technologies and building useful tools. I enjoy solving problems with code and aim to deliver efficient, scalable, and user-friendly solutions. I'm excited to contribute to meaningful projects and grow alongside a passionate team.")

    def __str__(self):
        return "About Page Content"

class SkillCategory(models.Model):
    """Model to categorize skills."""
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=50, help_text="Boxicons class, e.g., 'bx bx-code-alt'")
    order = models.IntegerField(default=0, help_text="Order in which categories appear")

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.name

class Skill(models.Model):
    """Model to store individual skills."""
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0, help_text="Order in which skills appear within their category")

    class Meta:
        ordering = ['category__order', 'order']

    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Project(models.Model):
    """Model to store portfolio projects."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/') # Re-added ImageField here
    live_link = models.URLField(max_length=500, blank=True, null=True)
    github_link = models.URLField(max_length=500, blank=True, null=True)
    order = models.IntegerField(default=0, help_text="Order in which projects appear")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class ContactDetail(models.Model):
    """Model to store various contact details."""
    type = models.CharField(max_length=50, choices=[
        ('linkedin', 'LinkedIn'),
        ('email', 'Email'),
        ('phone', 'Phone'),
        ('whatsapp', 'WhatsApp'),
        ('github', 'GitHub'),
        ('instagram', 'Instagram'),
        ('leetcode', 'LeetCode'),
    ], unique=True)
    value = models.CharField(max_length=200, help_text="e.g., username for LinkedIn, email address, phone number")
    icon_class = models.CharField(max_length=50, blank=True, null=True, help_text="Boxicons or Tabler Icons class, e.g., 'bx bxl-linkedin'. Auto-filled if left empty.")
    url = models.URLField(max_length=500, blank=True, null=True, help_text="Full URL for the contact method")
    order = models.IntegerField(default=0, help_text="Order in which contact details appear")

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Contact Details"

    def __str__(self):
        return f"{self.get_type_display()}: {self.value}"

    def save(self, *args, **kwargs):
        # Automatically set icon_class based on type if not already set
        if not self.icon_class:
            icon_map = {
                'linkedin': 'bx bxl-linkedin',
                'email': 'bx bx-envelope',
                'phone': 'bx bx-phone',
                'whatsapp': 'bx bxl-whatsapp',
                'github': 'bx bxl-github',
                'instagram': 'bx bxl-instagram',
                'leetcode': 'ti ti-brand-leetcode', # Using Tabler Icons for LeetCode
            }
            self.icon_class = icon_map.get(self.type, 'bx bx-info-circle') # Default icon if type not found
        super().save(*args, **kwargs)

class ContactMessage(models.Model):
    """Model to store messages submitted via the contact form."""
    full_name = models.CharField(max_length=200)
    email_address = models.EmailField()
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    email_subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"Message from {self.full_name} ({self.email_address})"