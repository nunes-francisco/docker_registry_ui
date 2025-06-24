document.getElementById('list-images').addEventListener('click', async () => {
    const response = await fetch('/docker/images');
    const data = await response.json();
    const imagesDiv = document.getElementById('images');
    imagesDiv.innerHTML = '';

    data.repositories.forEach(image => {
        const imageDiv = document.createElement('div');
        imageDiv.innerHTML = `
            <p>${image}</p>
            <button onclick="deleteImage('${image}')">Delete</button>
        `;
        imagesDiv.appendChild(imageDiv);
    });
});

async function deleteImage(imageName) {
    const response = await fetch(`/docker/images/${imageName}`, { method: 'DELETE' });
    const data = await response.json();
    alert(data.message);
}
