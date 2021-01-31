/**
 * Site JavaScript Here
 */

// console.log("Hello, World!");

function send() {
        var txt = document.getElementById("entryField").value
        document.getElementById("entryField").value = ""
        var node =  document.createElement("li");
        var right = document.getElementsByClassName("chat-right")
        var left = document.getElementsByClassName("chat-left")
        var l = left.length
        var r = right.length
        var rightItem = right[r -1].cloneNode(true)
        var leftItem = left[l -1].cloneNode(true)
        rightItem.getElementsByClassName("chat-text")[0].innerText = txt
        var tt = 'Im grand, thanks for asking. How has business  been? And sure, I would be down to get drinks later if you are.'
        leftItem.getElementsByClassName("chat-text")[0].innerText = tt
        document.getElementById("chatting").appendChild(rightItem)

        setTimeout(slll, 5000 ,leftItem)
}

function slll(elem) {
    const sleep = promisify(setTimeout)
    sleep(5000).then(() => {
        document.getElementById("chatting").appendChild(elem)
        });
}
