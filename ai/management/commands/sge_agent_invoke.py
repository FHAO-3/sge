from django.core.management.base import BaseCommand
from ai.agent import SGEAgent


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write(
            msg='Iniciando a analize do banco de dados ...'
        )
        agent = SGEAgent()
        agent.invoke()
        self.stdout.write(
            self.style.SUCCESS('Analize do banco de dados realizada com sucesso!')
        )
