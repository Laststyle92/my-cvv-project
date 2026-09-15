document.addEventListener('DOMContentLoaded', function() {
    const pages = document.querySelectorAll('.book-page');
    const prevBtn = document.getElementById('prev-page-btn');
    const nextBtn = document.getElementById('next-page-btn');
    const pageIndicator = document.getElementById('page-indicator');

    let currentPage = 1;
    const totalPages = pages.length;

    function updateBook() {
        pages.forEach((page, index) => {
            if (index + 1 === currentPage) {
                page.classList.add('active');
            } else {
                page.classList.remove('active');
            }
        });

        if (pageIndicator) {
            pageIndicator.textContent = `Страница ${currentPage} из ${totalPages || 1}`;
        }

        if (prevBtn) prevBtn.disabled = (currentPage === 1);
        if (nextBtn) nextBtn.disabled = (currentPage === totalPages || totalPages === 0);
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', function() {
            if (currentPage < totalPages) {
                currentPage++;
                updateBook();
            }
        });
    }

    if (prevBtn) {
        prevBtn.addEventListener('click', function() {
            if (currentPage > 1) {
                currentPage--;
                updateBook();
            }
        });
    }

    updateBook();
});