from django.core.management.base import BaseCommand
from questions.models import Question

class Command(BaseCommand):
    help = 'Loads initial GK questions'

    def handle(self, *args, **kwargs):
        questions_data = [
            {
                "question_text": "What is the capital of India?",
                "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
                "correct_answer": "New Delhi"
            },
            {
                "question_text": "Who wrote 'Romeo and Juliet'?",
                "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
                "correct_answer": "William Shakespeare"
            },
            {
                "question_text": "What is the largest planet in our solar system?",
                "options": ["Mars", "Saturn", "Jupiter", "Neptune"],
                "correct_answer": "Jupiter"
            },
            {
                "question_text": "Which element has the chemical symbol 'O'?",
                "options": ["Gold", "Oxygen", "Osmium", "Oganesson"],
                "correct_answer": "Oxygen"
            },
            {
                "question_text": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
                "correct_answer": "Pacific Ocean"
            },
            {
                "question_text": "Who painted the Mona Lisa?",
                "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"],
                "correct_answer": "Leonardo da Vinci"
            },
            {
                "question_text": "What is the currency of Japan?",
                "options": ["Won", "Yuan", "Yen", "Ringgit"],
                "correct_answer": "Yen"
            },
            {
                "question_text": "Which planet is known as the Red Planet?",
                "options": ["Venus", "Mars", "Jupiter", "Mercury"],
                "correct_answer": "Mars"
            },
            {
                "question_text": "What is the smallest prime number?",
                "options": ["0", "1", "2", "3"],
                "correct_answer": "2"
            },
            {
                "question_text": "Who is known as the father of computers?",
                "options": ["Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs"],
                "correct_answer": "Charles Babbage"
            }
        ]

        for question_data in questions_data:
            Question.objects.create(**question_data)
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded initial questions'))