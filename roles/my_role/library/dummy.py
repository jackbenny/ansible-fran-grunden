#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule

def run_module():
    # definiera argument till modulen
    module_args = dict(
        number=dict(type='int', required=True),
        )

    # skapa en dict för resultatet
    result = dict(
        changed=False,
        number=0,
        )

    # inställningar för modulen
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
        )

    # logiken för modulen
    result['number'] = module.params['number']
    if result['number'] > 50:
        result['changed']=True

    # returnera resultatet som json
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()

