function filterByCategory(category) {
    // Get all li elements
    const items = document.querySelectorAll('li[data-category]');

    // Loop through all li elements
    items.forEach(item => {
        // Check if the data-category of the item matches the category parameter
        if (item.getAttribute('data-category') === category || category === 'all') {
            // If it matches, ensure the item is visible
            item.style.display = '';
        } else {
            // If it does not match, hide the item
            item.style.display = 'none';
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    // Select all span elements with the class 'tag' that are within a 'section'
    const tags = document.querySelectorAll('section span.tag');

    // Add click event listener to each tag
    tags.forEach(tag => {
        tag.addEventListener('click', function() {
            // Remove the 'active' class from all tags in the section
            tags.forEach(t => t.classList.remove('active'));
            
            // Add the 'active' class to the clicked tag
            this.classList.add('active');
            filterByCategory(this.innerText);
        });
    });

    document.addEventListener("keypress", (event) => {
        const baseURL = "https://github.dev/dalleng/til"
        let goToURL = baseURL;
        if (window.location.pathname.startsWith("/site")) {
            const category = document.querySelector("meta[name='category']").content;
            const htmlPath = window.location.pathname.split('/').at(-1);
            const [title, _] = htmlPath.split('.');
            const filePath = `/blob/main/${category}/${title}.md`;
            goToURL = baseURL + filePath;
        }
        if (event.key === '.') {
            window.location = goToURL;
        }
    });
});