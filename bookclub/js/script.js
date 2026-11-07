// Login:checks the boxes are filled then redirects
function login() {
  var name = document.getElementById("username").value;
  var pass = document.getElementById("password").value;
  if (name == "" || pass == "") {
    alert("Please enter your username and password");
  } else {
    window.location.href = "index.html";
  }
}

// Books page : vote for a book
function vote(bookName) {
  document.getElementById("voteMessage").innerHTML = "Thanks! Your vote for " + bookName + " has been recorded.";
}

// Books page: suggest a book
function suggestBook() {
  var title = document.getElementById("bookTitle").value;
  if (title == "") {
    alert("Please enter a book title");
  } else {
    document.getElementById("suggestMessage").innerHTML = "Thanks! " + title + " has been suggested.";
    document.getElementById("bookTitle").value = "";
    document.getElementById("bookAuthor").value = "";
  }
}

// Meetings page: join a meeting
function joinMeeting(buttonId) {
  document.getElementById(buttonId).innerHTML = "Joined";
}

// Discussions page: add a comment to the list
function addComment() {
  var name = document.getElementById("commentName").value;
  var text = document.getElementById("commentText").value;
  if (name == "" || text == "") {
    alert("Please enter your name and a comment");
  } else {
    var list = document.getElementById("commentList");
    list.innerHTML = list.innerHTML + "<li><b>" + name + ":</b> " + text + "</li>";
    document.getElementById("commentName").value = "";
    document.getElementById("commentText").value = "";
  }
}
