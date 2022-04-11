const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('<script>window.location.replace("http://www.google.com");</script>')
})

app.get('/ballot-data', (req, res) => {
    console.log(req.query)
    res.send('<script>window.location.replace("http://www.google.com");</script>')
})

app.listen(port, () => {
  console.log(`Listening at http://localhost:${port}`)
})