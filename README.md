# 软件使用说明

### Django

请先配置 Django_projects/Software_design/Software_design/settings 文件中的MySQL的”DATABASES”和Django_projects/Software_design/my_app/llm-api中的“api-key”

```jsx
cd Django_Projects
cd Software_design
//配置MYSQL数据库
python python manage.py makemigrations my_app
python manage.py migrate
//运行
python manage.py runserver
```

### Vue

```jsx
cd vue_projects
npm install
//运行
npm run dev
```





