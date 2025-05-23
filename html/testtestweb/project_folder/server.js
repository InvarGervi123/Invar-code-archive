const express = require("express");
const multer = require("multer");
const path = require("path");
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.static("public")); // Публичные ресурсы (HTML, CSS, JS)

// Настройка Multer для загрузки медиа
const storage = multer.diskStorage({
    destination: "./public/media",
    filename: (req, file, cb) => {
        const uniqueSuffix = Date.now() + "-" + Math.round(Math.random() * 1E9);
        cb(null, file.fieldname + "-" + uniqueSuffix + path.extname(file.originalname));
    },
});

const upload = multer({ storage });

// Загрузка медиа
app.post("/upload", upload.single("media"), (req, res) => {
    // Обработка загрузки медиа, например, сохранение пути к файлу в базе данных
    // И возвращение успешного ответа
    res.sendStatus(200);
});

// Получение информации о медиа
app.get("/media", (req, res) => {
    // Здесь можно вернуть список медиа файлов из базы данных
    // Пример формата ответа: [{ type: "image/jpeg", url: "/media/file.jpg" }]
    res.json([]);
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
