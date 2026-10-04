def generateticket(event):
 
genre = document.querySelector("#genre").value
title = document.querySelector("#title").value
movielength = document.querySelector("#movielength").value

answer = "/".join([genre, title, movielength])

       document.querySelector("#skuticket").innerText = (
        "Result: " + answer
    )