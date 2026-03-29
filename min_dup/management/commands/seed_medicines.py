from django.core.management.base import BaseCommand

from min_dup.models import Medicine


class Command(BaseCommand):
    help = "Seed sample Medicine data (default: 20 rows)"

    def add_arguments(self, parser):
        parser.add_argument("--count", type=int, default=20)
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete existing Medicine rows before seeding",
        )

    def handle(self, *args, **options):
        count = options["count"]
        clear = options["clear"]

        if clear:
            deleted, _ = Medicine.objects.all().delete()
            self.stdout.write(self.style.WARNING(f"Cleared Medicine rows: {deleted}"))

        samples = [
            ("타이레놀정 500mg", "아세트아미노펜", "한국존슨앤드존슨"),
            ("게보린정", "아세트아미노펜", "삼진제약"),
            ("펜잘큐정", "아세트아미노펜", "종근당"),
            ("부루펜정", "이부프로펜", "삼일제약"),
            ("애드빌정", "이부프로펜", "화이자"),
            ("탁센연질캡슐", "나프록센", "종근당"),
            ("나프록센정", "나프록센", "대웅제약"),
            ("아스피린장용정", "아세틸살리실산", "바이엘"),
            ("로사르탄정", "로사르탄", "한미약품"),
            ("암로디핀정", "암로디핀", "대원제약"),
            ("오메프라졸캡슐", "오메프라졸", "종근당"),
            ("판토프라졸정", "판토프라졸", "대웅제약"),
            ("클로르페니라민정", "클로르페니라민", "유한양행"),
            ("세티리진정", "세티리진", "한독"),
            ("로라타딘정", "로라타딘", "동아ST"),
            ("아목시실린캡슐", "아목시실린", "GC녹십자"),
            ("세파클러캡슐", "세파클러", "한미약품"),
            ("메트포르민정", "메트포르민", "대웅제약"),
            ("글리메피리드정", "글리메피리드", "유한양행"),
            ("아토르바스타틴정", "아토르바스타틴", "종근당"),
        ]

        created = 0
        for name, ingredient, company in samples[:count]:
            _, was_created = Medicine.objects.get_or_create(
                name=name,
                ingredient=ingredient,
                defaults={"company": company},
            )
            if was_created:
                created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seed complete. requested={count}, created={created}, existing={count - created}"
            )
        )
