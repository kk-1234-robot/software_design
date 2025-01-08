# 软件使用说明

## 配置运行软件

### Django

请先配置 Django_projects/Software_design/Software_design/settings 文件中的MySQL的”DATABASES”和Django_projects/Software_design/my_app/llm-api中的“api-key”

```jsx
cd Django_Projects
cd Software_design
//配置MYSQL数据库中的表
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

## 使用步骤

### 首页

在首页中也可以查看对应的使用说明

### 上传标注任务

- 点击左侧标注任务框，跳转到标注任务界面，输入标注任务名称以及轮次，最后将.csv文件拖入上传文件框中（或点击上传文件框再选择文件路径），上传文件。

- 点击左侧标注框，跳转到标注界面。

- 点击上一份或下一份按键切换标注的按键

- 在案件文本框内修改案件后点击更新案件可以将案件信息更新

- 点击上一句或下一句切换标注的句子

- 开始标注

  - 点击智能标注，可以将本句词语进行自动标注
  - 点击上一个词或者下一个词可以查看本句中不同词语的标注情况，点击词性和实体按键可以看到其标注的词性和实体，勾选其下拉的选项后点击提交选择可以修改词性和实体标注情况

- 查看结果：点击左侧结果框，跳转到结果界面可以查看所有已标注案件中的词性和实体分别情况

- 保存结果：在结果界面点击导出数据可以将标注的数据导出

  





### 



