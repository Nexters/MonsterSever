## 게임팀 서버!

### Requirement
- Python 3.4.2(pyenv)
    - python --version
- Django 1.7.4
    - python -c "import django; print(django.get_version())" 

### 장고 명령어 
- django-admin.py startproject mysite : 프로젝트생
- python manage.py startapp models : 모델 생성 (모델 이름을 calmelize 하고 s inflect)
- python manage.py runserver 8080 : 서버 실행
- python manage.py makemigrations models : migration sql 파일 만들기
- python manage.py sqlmigrate models 0001 : 0001번호에 맞는 sql 실행
    - 필드를 추가하면 자동적으로 add Column 을 하는 migration 파일을 생성
- python manage.py migrate : migrate 실행
- python manage.py shell : shell 에서 테스트
    - django_extensions 를 설치해서 python manage.py shell_plus 로 모델 자동 추


### INSTALLED_APPS
#### django_extensions
- python manage.py graph_models -a -o myapp_models.png
- python manage.py show_urls
- python manage.py validate_templates
- python manage.py shell_plus
- python manage.py runserver_plus
