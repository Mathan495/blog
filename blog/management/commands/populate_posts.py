from blog.models import Post,Category
from django.core.management.base import BaseCommand 
import random


class Command(BaseCommand):
    help = "This commandes inserts post data"

    def handle(self, *args, **options):

        # Delete existing Data
        Post.objects.all().delete()

        category = Category.objects.first()
        
        titles = [
    "The Art of Starting Before You re Ready",
    "Tiny Habits That Changed My Life in 30 Days",
    "Why Doing Nothing Might Be Your Most Productive Move",
    "A Beginners Guide to Reinventing Yourself",
    "Lessons I Learned from Failing Publicly",
    "Deep Work in a Distracted World",
    "The 5-Minute Rule That Beats Procrastination",
    "How to Design a Morning Routine That Actually Sticks",
    "Burnout Isn’t Laziness: Here’s the Difference",
    "Systems Over Goals: The Smarter Way to Succeed"
]
        content = [
            "Why imperfect action beats endless planning every single time.",
            "Small daily changes can quietly create massive long-term results.",
            "Strategic rest can boost creativity, clarity, and better decision-making",
            "Simple steps to reset your mindset, habits, and direction at any stage of life.",
            "How visible mistakes can become your greatest growth opportunities.",
            "Practical ways to focus deeply and produce meaningful results in a noisy environment.",
            "Starting for just five minutes can break the cycle of delay and overwhelm.",
            "Build a realistic morning system that supports your goals without burnout.",
            "Understanding the signs of burnout can help you recover without guilt.",
            "Sustainable systems create consistent success more reliably than big goals alone."
        ]

        img_url = [
            "https://picsum.photos/id/1/800/400",
            "https://picsum.photos/id/2/800/400",
            "https://picsum.photos/id/3/800/400",
            "https://picsum.photos/id/4/800/400",
            "https://picsum.photos/id/5/800/400",
            "https://picsum.photos/id/6/800/400",
            "https://picsum.photos/id/7/800/400",
            "https://picsum.photos/id/8/800/400",
            "https://picsum.photos/id/9/800/400",
            "https://picsum.photos/id/10/800/400",
            "https://picsum.photos/id/11/800/400",
            "https://picsum.photos/id/12/800/400",
            "https://picsum.photos/id/13/800/400",
            "https://picsum.photos/id/14/800/400",
            "https://picsum.photos/id/15/800/400",
            "https://picsum.photos/id/16/800/400",
            "https://picsum.photos/id/17/800/400",
            "https://picsum.photos/id/18/800/400",
            "https://picsum.photos/id/19/800/400",
            "https://picsum.photos/id/20/800/400",
        ]

        catagories = Category.objects.all()
        for title, content, img_url in zip(titles, content, img_url):
            category = random.choice(catagories)
            Post.objects.create(title=title, content=content, img_url=img_url,category=category) 

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!")) 