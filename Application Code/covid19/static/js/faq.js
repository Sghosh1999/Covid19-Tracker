const answer = document.querySelector('.answer');

function seeHideAnswer(ar, q) {

    const arrowClass = document.querySelector('.arrow' + ar + ' i');
    const question = document.querySelector('.' + q);


    if (arrowClass.classList.contains('fa-arrow-down')) {
        arrowClass.classList.remove('fa-arrow-down');
        arrowClass.classList.add('fa-arrow-up');
        question.classList.remove('hide');
    } else {
        arrowClass.classList.remove('fa-arrow-up');
        arrowClass.classList.add('fa-arrow-down');
        question.classList.add('hide');
    }
}