import operations as o


args_to_operations = {
    'info': ('', o.info),

    'commands': ('', o.commands),

    'list envs': ('', o.list_envs),

    'env info': ('i', o.env_info),

    'env info more': ('i', o.env_info_more),

    'info <env_name>': ('', o.env_info_outside),

    'info <env_name> more': ('', o.env_info_outside_more),

    'create <env_name>': ('o', o.create),

    'create <env_name> overwrite': ('o', o.create_overwrite),

    'remove <env_name>': ('o', o.remove),

    'install <package_name> <package_version>': ('i', o.install),

    'install <package_name>': ('i', o.install),

    'clone <current_env> to <new_env>': ('o', o.clone),

    'clone <new_env> from <current_env>': ('o', o.clone),

    'clone <current_env> upto version <version_number> as <new_env>': ('o', o.clone),

    'clone <new_env> upto version <version_number> from <current_env>': ('o', o.clone),

    'export <file_name>': ('', o.export),

    'build <file_path> to <env_name>': ('o', o.build),

    'build <env_name> from <file_path>': ('o', o.build)
}