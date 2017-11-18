module.exports = {
  entry: __dirname + '/client/src/index.js',
  output: {
    path: __dirname + '/client/public',
    filename: 'bundle.js'
  },
  module: {
    loaders: [
      {
        test: /\.js(x)?$/,
        include: __dirname + '/client/src',
        loader: 'babel-loader'
      }
    ]
  }
}
