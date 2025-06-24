document.getElementById('list-images').addEventListener('click', async () => {
    const response = await fetch('/docker/images');
    const data = await response.json();
    const imagesDiv = document.getElementById('images');
    const imageSelect = document.getElementById('image-select');
    imagesDiv.innerHTML = '';
    imageSelect.innerHTML = '';

    data.repositories.forEach(image => {
        const imageDiv = document.createElement('div');
        imageDiv.innerHTML = `
            <p>${image}</p>
        `;
        imagesDiv.appendChild(imageDiv);

        const option = document.createElement('option');
        option.value = image;
        option.text = image;
        imageSelect.appendChild(option);
    });

    document.getElementById('delete-form').style.display = 'block';
});

document.getElementById('delete-image-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const imageSelect = document.getElementById('image-select');
    const imageName = imageSelect.value;
    const response = await fetch(`/docker/images/${imageName}`, { method: 'DELETE' });
    const data = await response.json();
    alert(data.message);
    imageSelect.remove(imageSelect.selectedIndex);
});
