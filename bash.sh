# 打印启动信息
echo "starting Bot ~@DroneBots"

# 启动 Flask 应用（如果需要）
echo "正在启动 Flask 应用..."
flask run -h 0.0.0.0 -p 5000 &

# 启动 Python 主程序
echo "正在启动 Python 主程序..."
python3 -m main
