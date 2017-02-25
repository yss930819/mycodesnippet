module.exports ={
    devtool: 'eval-source-map',//配置生成Source Maps，选择合适的选项
    //可选项 见http://blog.csdn.net/kun5706947/article/details/52596766

    entry: __dirname + "/app/main.js", //已多次提及的唯一入口文件
    output: {
        path: __dirname + "/public", //打包后的文件存放的地方
        filename: "bundle.js" //打包后输出文件的文件名
    }
}