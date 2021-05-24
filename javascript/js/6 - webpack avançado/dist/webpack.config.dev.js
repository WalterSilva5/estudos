"use strict";

var webpack = require('webpack');

var path = require('path');

var UglifyJsPlugin = require('uglifyjs-webpack-plugin');

module.exports = {
  devtool: 'source-map',
  entry: './src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist')
  },
  module: {
    rules: [{
      test: /\.jsx?$/,
      include: /\.js$/,
      exclude: /\/node_modules/
    }]
  },
  optimization: {
    minimizer: [new UglifyJsPlugin({
      uglifyOptions: {
        warnings: false,
        parse: {},
        compress: {},
        mangle: true,
        // Note `mangle.properties` is `false` by default.
        output: null,
        toplevel: false,
        nameCache: null,
        ie8: false,
        keep_fnames: false
      },
      extractComments: /@extract/i
    })]
  }
};