var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')
var frontend = path.resolve(__dirname, '../../frontend/')
var backend = path.resolve(__dirname, '../../backend/')

module.exports = {
  context: __dirname,

  entry: {
    main: [
      path.resolve(frontend, 'libraries/base_theme/js/index')
    ],
    blog_post: [
      path.resolve(frontend, 'libraries/blog/js/index')
    ]
  },

  output: {
    path: path.resolve(backend, 'iamsitting_site/static/bundles/'),
    filename: "[name].js",
  },

  plugins: [
    new BundleTracker({path: __dirname, filename: './webpack-stats.json'}),
    new webpack.IgnorePlugin(/^\.\/locale$/, /moment\/js$/), // to not to load all locales
    new webpack.ProvidePlugin({
      $: "jquery",
      jQuery: "jquery"
    }),
  ],

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: [/node_modules/],
        use: [
          {
            loader: 'babel-loader',
          }
        ]
      }, //js, jsx
      {
        test: /\.woff2?$|\.ttf$|\.eot$|\.svg$|\.png$|\.jpg$|\.gif$/,
        loader: [
        {
          loader: 'file-loader',
          options: {
            name: '[name]-[hash].[ext]'
          }
        }
        ]
      }
    ],
  },

  resolve: {
    modules: [
      path.resolve(__dirname, '../node_modules'),
      path.resolve(__dirname, '../libraries'),
    ],
    alias: {
      jquery: "jquery/src/jquery"
    }
  }
}

