import {BlogPost} from './models'

const routeHome = ['get', 'blog/',
  function(context){
    console.log('hello1');
    BlogPost.getPosts().then(function(data, context){
      console.log(data);
      $.each(data, function(i, item) {
        context.log(item.title, item.subtitle, item.author);
      });
    });
    // context.app.swap('');
    console.log(context);
    //context.render('templates/home.hb', {}).appendTo(context.$element());
    this.partial('/blog/templates/home.hb')
  }
];

const routeNewPost = ['get', '#/new-post',
  function(){
  }
]

const routeEditPost = ['get', '#/edit-post',
  function(){
  }
]

const routeViewPost = ['get', '#/view-post',
  function(){
  }
]

const routePostRequests = ['get', '#/post-requests',
  function(){
  }
]

const routeArchives = ['get', '#/archives',
  function(){

  }
]

const routeTemplates = ['get', 'templates/home.hb',
  function(context){
    console.log('hi2');
  }
]

export const appRoutes = [
  routeHome,
  routeNewPost,
  routeEditPost,
  routeViewPost,
  routePostRequests,
  routeArchives,
  routeTemplates
]
