document.addEventListener("DOMContentLoaded", function () {
    const mediaInput = document.getElementById("mediaInput");
    const uploadButton = document.getElementById("uploadButton");
    const mediaGallery = document.getElementById("mediaGallery");

    uploadButton.addEventListener("click", async function () {
        const file = mediaInput.files[0];
        if (file) {
            const formData = new FormData();
            formData.append("media", file);

            const response = await fetch("/upload", {
                method: "POST",
                body: formData,
            });

            if (response.ok) {
                // Обновить галерею после успешной загрузки
                updateMediaGallery();
            }
        }
    });

    async function updateMediaGallery() {
        const response = await fetch("/media");
        if (response.ok) {
            const mediaData = await response.json();
            mediaGallery.innerHTML = ""; // Очистить галерею

            mediaData.forEach((item) => {
                const mediaContainer = document.createElement("div");
                mediaContainer.classList.add("media-container");

                if (item.type.startsWith("image")) {
                    const img = document.createElement("img");
                    img.src = item.url;
                    mediaContainer.appendChild(img);
                } else if (item.type.startsWith("video")) {
                    const video = document.createElement("video");
                    video.src = item.url;
                    video.controls = true;
                    mediaContainer.appendChild(video);
                }

                mediaGallery.appendChild(mediaContainer);
            });
        }
    }

    // При загрузке страницы, обновить галерею
    updateMediaGallery();
});
