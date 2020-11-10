// Create a request variable and assign a new XMLHttpRequest object to it.

function getGear(){
  var request = new XMLHttpRequest()

  // Open a new connection, using the GET request on the URL endpoint
  request.open('GET', 'https://api.osrsbox.com/items', true)

  request.onload = function () {
    console.log("here")
    var data = JSON.parse(this.response)
    data.forEach((item) => {
        console.log(item)
    })
  }
  // Send request
  request.send()
}