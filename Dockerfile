# استخدم صورة Python الأساسية
FROM python:3.10

# تثبيت curl للتحقق من الاتصال
RUN apt-get update --fix-missing && apt-get install -y curl

# تحديث الحزم وتثبيت الأدوات المطلوبة مع عرض التفاصيل
RUN apt-get update --fix-missing && apt-get install -y \
    build-essential \
    libmariadb-dev-compat \
    libmariadb-dev \
    && echo "APT INSTALL SUCCESS" \
    || { echo "apt-get install failed"; exit 1; }

# حدد مجلد العمل داخل الحاوية
WORKDIR /app

# انسخ الملفات إلى الحاوية
COPY . .

# تثبيت الحزم من requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# قم بتشغيل التطبيق
CMD ["python", "manage.py", "runserver"]
