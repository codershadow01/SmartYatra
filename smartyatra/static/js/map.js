// let sidebar = document.getElementsByClassName("col-md-8")[0];
// let sidebar_content = document.getElementsByClassName("map-wrapper")[0];

// window.onscroll = () => {
//     let scrollTop
// }


window.onscroll = function() {
    var scrollSection = document.querySelector('.detail');
    var fixedSection = document.querySelector('.map-wrapper');

    var scrollSectionOffset = scrollSection.getBoundingClientRect().top;
    var fixedSectionHeight = fixedSection.offsetHeight;

    if (scrollSectionOffset <= fixedSectionHeight) {
        fixedSection.style.top = (fixedSectionHeight - scrollSectionOffset) + 'px';
    } else {
        fixedSection.style.top = '0';
    }
};