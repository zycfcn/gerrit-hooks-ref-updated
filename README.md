# gerrit-hooks-ref-updated
基于gerrit 的hooks 插件，用python 写的ref-updated webhooks,可发送给多个接收服务器

gerrit 最少版本2.15
python 版本 2.7.x

如果你的gerrit 版本小于2.15请升级到最新，gerrit 升级注意事项: 需要递增式升级，切记不要跨版本升级

等做完以上事项，并安装好hooks 插件，只需要把 本仓库的 ref-updated 文件放到 gerrit_home/hooks/ref-updated

并给ref-updated 文件执行权限即可


# 参数可打开文件根据自己实际情况修改
