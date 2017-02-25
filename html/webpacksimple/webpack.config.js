module.exports = {
    devtool: 'eval-source-map', //配置生成Source Maps，选择合适的选项
    entry: __dirname + "/app/main.js", //已多次提及的唯一入口文件
    output: {
        path: __dirname + "/public", //打包后的文件存放的地方
        filename: "bundle.js" //打包后输出文件的文件名
    },

    module: { //在配置文件里添加JSON loader
        loaders: [{
                test: /\.json$/,
                loader: "json-loader"
            },
            { //配置使用babel
                test: /\.js$/,
                exclude: /node_modules/,
                loader: 'babel-loader', //在webpack的module部分的loaders里进行配置即可
                query: {
                    presets: ['es2015', 'react']
                }
            },
            {
                test: /\.css$/,
                loader: 'style-loader!css-loader' //添加对样式表的处理
            }
        ]
    },

    devServer: {
        contentBase: "./public", //本地服务器所加载的页面所在的目录
        compress: true, 
        historyApiFallback: true, //不跳转
        port: 9000,
    }
}