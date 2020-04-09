/* Loader */
const loader = document.querySelector('.loader');
const postLoader = document.querySelector('.post-loader');

// After 3 seconds
setTimeout(() => {
    loader.classList.add('hide');
    postLoader.classList.remove('hide');
}, 3000);