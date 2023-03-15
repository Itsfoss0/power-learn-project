let totalVotes = 0;
const votesContent = document.getElementById('votes');
const upvoteButton = document.getElementById('upvote');
const downvoteButton = document.getElementById('downvote');

console.log(votesContent.innerHTML);

upvoteButton.addEventListener('click', () => {
  totalVotes += 1;
  votesContent.textContent = `${totalVotes} Votes`;
});

downvoteButton.addEventListener('click', () => {
  totalVotes -= 1;
  votesContent.textContent = `${totalVotes} Votes`;
});
