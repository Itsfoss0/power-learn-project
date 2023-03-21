let totalVotes = 0;
const votesContent = document.getElementById('votes');
const upvoteButton = document.getElementById('upvote');
const downvoteButton = document.getElementById('downvote');
const question = document.getElementById('question');
const originalQuestion = question.innerHTML;

console.log(votesContent.innerHTML);

upvoteButton.addEventListener('click', () => {
  totalVotes += 1;
  votesContent.textContent = `${totalVotes} Votes`;
  if (question.textContent !== originalQuestion) {
    question.textContent = originalQuestion;
  }
});

downvoteButton.addEventListener('click', () => {
  totalVotes -= 1;
  if (totalVotes < 0) {
    question.textContent = 'Question downvoted to hell !!';
  }
  votesContent.textContent = `${totalVotes} Votes`;
});
