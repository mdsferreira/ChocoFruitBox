from celery.registry import task
from celery.task import Task
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone
from django.contrib.auth.models import User

class sendRemmendationsEmailTask(Task):

    def run(self):
        users = User.objects.all()
        for user in users :
            recommendation = 1 #SuperChoc.get_recommendations(white_choc=1, dark_choc=3)
            from_email = "chocofruit@chocofruit.com"
            subject, to = "Your recommended ChocoFruit box is ready", user.email
            html_content = '''
            <html>
                <body>
                <p>Hi %s!, </p>
                <p>Your recommended ChocoFruit box is ready. Login our <a href='#'>website</a> and check 
                it out.</p>
                </body>
            </html>'''% user.first_name
            text_content = strip_tags(html_content)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        print("%d emails send with success!" %  timezone.now)

task.register(sendRemmendationsEmailTask)

        