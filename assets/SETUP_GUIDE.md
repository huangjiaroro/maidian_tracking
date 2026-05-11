# manage-tracking 安装与配置引导

## 概览

这份文档用于指导 `manage-tracking` 的首次初始化流程。

推荐先直接执行：

```bash
manage-tracking auth whoami
```

这个命令最接近真实使用场景，能帮助判断：

- CLI 是否已安装
- 当前证书、URL、认证是否可用
- 后端是否能识别当前用户

## 第 1 步：先尝试 `auth whoami`

```bash
manage-tracking auth whoami
```

根据结果处理：

- 成功返回用户信息：安装和核心配置已经基本完成
- shell 提示 `command not found`：CLI 还没安装，继续第 2 步
- 命令存在，但报证书、URL、认证或 API 错误：CLI 已安装，但配置还没完成，继续第 3 步

## 第 2 步：安装 skill 自带 CLI

在 skill 根目录执行：

```bash
bash ./skill-install.sh
./.skillhub/bin/manage-tracking --help
```

安装后优先再次执行：

```bash
./.skillhub/bin/manage-tracking auth whoami
```

如果仍然是配置相关错误，再进入下一步。

## 第 3 步：配置连接与认证

### 推荐方式：使用 SkillHub 共享配置

优先准备：

- 配置文件路径：`$HOME/.skillhub-cli/config.json`

示例：

```json
{
  "ssl_cert_file": "/path/to/client_cert.p12",
  "ssl_cert_password": "YOUR_CERT_PASSWORD",
  "user_email": "your_email@example.com"
}
```

然后重新执行：

```bash
bash ./skill-install.sh
./.skillhub/bin/manage-tracking --json config show
```

当前安装脚本会自动读取共享配置里的：

- `ssl_cert_file`
- `ssl_cert_password`
- `user_email`

如果你需要按 SkillHub 环境区分地址，还可以在 skill 私有配置里增加：

```json
{
  "office_base_url": "https://office.example.internal/maidian/server",
  "prod_base_url": "https://prod.example.internal/maidian/server"
}
```

当前代码会根据 `skillhub_env` 自动选择对应地址。

### 手动配置兜底方案

如果共享配置不存在，也可以手动执行：

```bash
./.skillhub/bin/manage-tracking config set-env prod
./.skillhub/bin/manage-tracking config set-cert /path/to/client_cert.p12 YOUR_CERT_PASSWORD
./.skillhub/bin/manage-tracking --json config show
```

如需自定义地址：

```bash
./.skillhub/bin/manage-tracking config set-url https://phonestat.hexin.cn/maidian/server
```

## 第 4 步：验证结果

先执行：

```bash
./.skillhub/bin/manage-tracking --json config show
```

至少确认：

- `base_url` 是你要使用的环境地址
- `has_cert` 为 `true` 时表示证书已经加载
- `email` 为当前用户邮箱

然后再次执行：

```bash
./.skillhub/bin/manage-tracking auth whoami
```

如果 `auth whoami` 成功返回用户信息，就可以认为安装和配置已经完成。
