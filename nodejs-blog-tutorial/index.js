const express = require('express');
const path = require('path');
var bodyParser = require('body-parser')
//const dbUtils = require('./dbutils');

// dbUtils.createModels();

var mongoose = require("mongoose");
mongoose.connect("mongodb://localhost:27017/mydb?authSource=admin",{
 "user": "admin",
 "pass": "success123",
 useNewUrlParser: true,
 useUnifiedTopology: true
 
}).then(()=>{
   console.log('successfully connected');
}).catch((err)=>{
       console.log('Error in connection');
});
var postSchema = new mongoose.Schema({ body: String });
var Post = mongoose.model('Post', postSchema);

 
const app = new express();

app.use(express.static('public'));


app.engine('html', require('ejs').renderFile);
app.set('view engine', 'html');

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true}))


app.get('/', (req, res) => {
    Post.find({}, (err, posts) => {
        res.render('index', { posts: posts})
    });
});

app.get('/about', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'pages/about.html'));
});

app.get('/contact', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'pages/contact.html'));
});
 
app.get('/post', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'pages/post.html'));
});

app.post('/addpost', (req, res) => {
    var postData = new Post(req.body);
    postData.save().then( result => {
        res.redirect('/');
    }).catch(err => {
        res.status(400).send("Unable to save data "+err);
    });
});
 
app.listen(3000, () => {
    console.log('App listening on port 3000')
});
