# ROS 2 System Monitor 作业

这是 RoboMaster 招新的 ROS 2 编程作业。你将从一个已经能运行的 ROS 2 基础工程开始，新增一个 `monitor_node`，观察系统中的传感器和目标状态。

## 环境

- Ubuntu 22.04
- ROS 2 Humble
- Python 3
- `colcon`

先加载 ROS 环境：

```bash
source /opt/ros/humble/setup.bash
```

## 基础工程

进入工作区并编译：

```bash
cd rm_demo_ws
colcon build --symlink-install
source install/setup.bash
```

启动基础系统：

```bash
ros2 launch rm_demo demo.launch.py
```

基础节点和通信关系：

```text
sensor_node --/sensor_data--> detector_node --/target--> controller_node
```

消息类型：

```text
/sensor_data  std_msgs/msg/Float32
/target       std_msgs/msg/Bool
```

传感器会周期性发布一组确定性的数值，`detector_node` 默认使用 `threshold=0.6` 判断是否发现目标。

## 作业要求

你需要新增 `monitor_node`，并把它加入 Python 包的 executable 配置和 `demo.launch.py`。

### 订阅

```text
/sensor_data  std_msgs/msg/Float32
/target       std_msgs/msg/Bool
```

### 发布

```text
/system_status  std_msgs/msg/String
```

### 参数

声明一个 ROS parameter：

```text
publish_period = 2.0
```

它控制 `/system_status` 的发布周期。launch 文件应支持：

```bash
ros2 launch rm_demo demo.launch.py publish_period:=0.5
```

### 状态内容

每条 `/system_status` 字符串至少表达：

- 最近一次 sensor 数值
- 最近一次 target 状态
- 累计收到的 sensor 消息数量

例如：

```text
sensor=0.75,target=true,count=8
```

字段顺序、空格和具体字符串格式可以自行设计，但语义必须清楚，`count` 必须随着收到 sensor 消息递增。

## 自测命令

查看节点：

```bash
ros2 node list
ros2 node info /monitor_node
```

查看话题和类型：

```bash
ros2 topic list -t
ros2 topic info /system_status -v
ros2 topic echo /system_status
```

检查参数：

```bash
ros2 param list /monitor_node
ros2 param get /monitor_node publish_period
```

检查 launch 参数效果：

```bash
ros2 launch rm_demo demo.launch.py publish_period:=0.5
ros2 topic hz /system_status
```

## 提交方式

1. 只修改你自己的 GitHub repository。
2. 不要修改或删除基础节点的核心行为。
3. 不要提交 `build/`、`install/`、`log/`、`.venv/` 等生成目录。
4. 提交前确认代码已经 `git add`、`git commit`、`git push`。
5. 请自建一个 GitHub repository，将本作业代码推送到自己的仓库。
6. 将 GitHub 仓库链接通过 QQ 私信发送给管理员，并备注姓名和学号。

## 常见问题

### `Package 'rm_demo' not found`

重新编译并 source：

```bash
colcon build --symlink-install
source install/setup.bash
```

### launch 找不到 `monitor_node`

检查 `setup.py` 的 `console_scripts` 和 `demo.launch.py` 是否都已经加入 `monitor_node`。

### 程序运行结果不符合预期

先在本地依次检查：节点列表、话题类型、`ros2 node info /monitor_node`、参数值、`ros2 topic echo /system_status` 和 launch 参数 `publish_period:=0.5`。

