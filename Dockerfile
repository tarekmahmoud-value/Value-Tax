# استخدام الصورة الأساسية
FROM python:3.8

# تعيين البيئة
ENV PYTHONUNBUFFERED=1

# تعيين دليل العمل
WORKDIR /app

# تحديث المستودعات وتثبيت الحزم المطلوبة
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libmysqlclient-dev \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* || cat /var/log/apt/term.log

# نسخ ملف المتطلبات
COPY requirements.txt /app/

# تثبيت المتطلبات من ملف requirements.txt
RUN pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي الملفات إلى الحاوية
COPY . /app

# تعيين المتغير اللازم لتهيئة Django
ENV DJANGO_SETTINGS_MODULE=VALUE.settings

# فتح المنفذ الذي سيعمل عليه الخادم
EXPOSE 8000

# تعيين نقطة البداية للتشغيل وتشغيل الخادم باستخدام Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
