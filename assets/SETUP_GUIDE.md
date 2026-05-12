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

- 配置文件路径：优先 `$HOME/.skillhub-cli/config.json`；如果不存在，再读取 `/root/.skillhub-cli/config.json`
- 不读取 `$HOME/.skillhub/config.json` 或 `/root/.skillhub/config.json`

示例：

```json
{
  "skillhub_env": "prod",
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

- `skillhub_env`
- `ssl_cert_file`
- `ssl_cert_password`
- `user_email`

当前代码只会根据共享配置里的 `skillhub_env` 自动选择地址；未配置或配置非法时默认使用 `prod`。技能本身不再保存私有环境配置，也不再提供技能私有配置的持久化命令。

`registry`、`openclaw_skill_dir`、`ssl_legacy_mode` 等字段属于 SkillHub CLI 安装 / 平台配置，不参与 manage-tracking 运行时鉴权。当前 `config show` / `ping` 输出不包含 `environment`、`has_token`；如果出现这些字段，说明执行到旧版 CLI 或旧 wrapper。

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
