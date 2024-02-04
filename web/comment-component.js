class CommentComponent extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });

        const template = document.createElement('template');
        template.innerHTML = `
            <style>
                :host {
                    display: block;
                    border: var(--comment-border, 1px solid #ddd);
                    border-radius: var(--comment-border-radius, 8px);
                    padding: var(--comment-padding, 16px);
                    margin: var(--comment-margin, 16px);
                    background-color: var(--comment-background-color, #fff);
                    box-shadow: var(--comment-box-shadow, 0 2px 4px rgba(0, 0, 0, 0.1));
                }

                .comment-content {
                    font-size: var(--comment-content-font-size, 16px);
                    margin-bottom: var(--comment-content-margin-bottom, 12px);
                }

                .comment-actions {
                    display: flex;
                    align-items: center;
                    gap: var(--comment-actions-gap, 12px);
                }

                .likeBtn {
                    display: flex;
                    align-items: center;
                    cursor: pointer;
                    color: var(--comment-like-color, #4CAF50);
                }

                .likeBtn span {
                    margin-right: var(--comment-like-span-margin, 5px);
                }

                .replyTextarea {
                    display: none;
                    width: 100%;
                    box-sizing: border-box;
                    margin-top: var(--comment-reply-textarea-margin-top, 8px);
                    padding: var(--comment-reply-textarea-padding, 8px);
                    border: var(--comment-reply-textarea-border, 1px solid #ddd);
                    border-radius: var(--comment-reply-textarea-border-radius, 4px);
                    resize: vertical;
                    font-size: var(--comment-reply-textarea-font-size, 14px);
                }

                .sendBtn {
                    display: none;
                    margin-top: var(--comment-send-btn-margin-top, 8px);
                    cursor: pointer;
                    background-color: var(--comment-send-btn-bg-color, #4CAF50);
                    color: var(--comment-send-btn-color, white);
                    border: var(--comment-send-btn-border, none);
                    padding: var(--comment-send-btn-padding, 8px 16px);
                    font-size: var(--comment-send-btn-font-size, 14px);
                    border-radius: var(--comment-send-btn-border-radius, 4px);
                }
            </style>
            <div class="comment">
                <div class="comment-content">
                    <slot></slot>
                </div>
                <div class="comment-actions">
                    <button class="replyBtn">Ответить</button>
                    <div class="likeBtn">
                        <span>👍</span>
                        <span class="likeCount">0</span>
                    </div>
                </div>
                <div class="replies"></div>
                <textarea class="replyTextarea" placeholder="Напишите свой комментарий"></textarea>
                <button class="sendBtn">Отправить</button>
            </div>
        `;

        this.shadowRoot.appendChild(template.content.cloneNode(true));

        this.shadowRoot.querySelector('.replyBtn').addEventListener('click', this.toggleReplyTextarea.bind(this));
        this.shadowRoot.querySelector('.likeBtn').addEventListener('click', this.like.bind(this));
        this.shadowRoot.querySelector('.sendBtn').addEventListener('click', this.sendReply.bind(this));

        // Счетчик лайков
        this.likeCount = 0;
        this.likeCountElement = this.shadowRoot.querySelector('.likeCount');
    }

    toggleReplyTextarea() {
        const replyTextarea = this.shadowRoot.querySelector('.replyTextarea');
        const sendBtn = this.shadowRoot.querySelector('.sendBtn');
        
        if (replyTextarea.style.display === 'none' || !replyTextarea.style.display) {
            replyTextarea.style.display = 'block';
            sendBtn.style.display = 'block';
        } else {
            replyTextarea.style.display = 'none';
            sendBtn.style.display = 'none';
        }
    }

    like() {
        this.likeCount++;
        this.likeCountElement.textContent = this.likeCount;
        this.dispatchEvent(new CustomEvent('like', { bubbles: true, composed: true }));
    }

    sendReply() {
        const replyTextarea = this.shadowRoot.querySelector('.replyTextarea');
        const replyText = replyTextarea.value.trim();
        
        if (replyText) {
            const replyElement = document.createElement('comment-component');
            replyElement.textContent = replyText;
            this.shadowRoot.querySelector('.replies').appendChild(replyElement);
            // Очищаем поле ввода после отправки
            replyTextarea.value = '';

            // Скрываем поле ввода и кнопку отправки после отправки комментария
            replyTextarea.style.display = 'none';
            this.shadowRoot.querySelector('.sendBtn').style.display = 'none';
        }
    }
}

customElements.define('comment-component', CommentComponent);
