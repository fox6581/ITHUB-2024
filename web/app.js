document.addEventListener('DOMContentLoaded', () => {
    const appContainer = document.getElementById('comments-app');

    const commentsData = [
        { text: 'Первый комментарий', replies: [{ text: 'Ответ на первый комментарий' }] },
        { text: 'Второй комментарий' },
        { text: 'Третий комментарий', replies: [{ text: 'Ответ на третий комментарий' }] },
    ];

    function createCommentElement(text) {
        const commentElement = document.createElement('comment-component');
        commentElement.textContent = text;
        return commentElement;
    }

    function renderComments(comments, container) {
        comments.forEach(commentData => {
            const commentElement = createCommentElement(commentData.text);
            container.appendChild(commentElement);

            if (commentData.replies && commentData.replies.length > 0) {
                const repliesContainer = commentElement.shadowRoot.querySelector('.replies');
                renderComments(commentData.replies, repliesContainer);
            }
        });
    }

    function handleLike(event) {
        console.log('Liked comment:', event.target.textContent.trim());
        // Здесь вы можете добавить свою логику для обработки лайков
    }

    // Перенесем слушатель события 'like' на элемент appContainer
    appContainer.addEventListener('like', handleLike);

    renderComments(commentsData, appContainer);
});
