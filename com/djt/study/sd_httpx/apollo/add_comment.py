"""
通过Http请求为配置添加注释
@author 　djt317@qq.com
@since 　 2023-09-27
"""
import json
from typing import List

import httpx

from com.djt.study.sd_httpx.apollo.comments import comments

# 获取项目环境与集群URL模板
url_get_env_cluster_template = 'http://apollo-ui-pro.jlpay.io/apps/{}/navtree'

# 获取配置URL模板
url_get_config_template = 'http://apollo-ui-pro.jlpay.io/apps/{}/envs/{}/clusters/{}/namespaces'

# 更新配置URL模板
url_put_config_template = 'http://apollo-ui-pro.jlpay.io/apps/{}/envs/{}/clusters/{}/namespaces/{}/item'

# 请求头
headers = {
    'Cookie': 'hash_fallback=9c34ab86-459d-45c7-80ad-d8e226cf9261; NG_TRANSLATE_LANG_KEY=zh-CN; '
              'sid=9fdc37fa-4df0-11ee-84c3-14fd33035894; JSESSIONID=CF68C82B27CFB6BB47A5416D5CBB0923'
}

# 待添加配置的项目列表
appid_list = ['RISKCTRL.risk-stat-payorder', 'RISKCTRL.risk-stat-payment', 'RISKCTRL.risk-stat-archive']


class ApolloInfo:
    """
    Apollo相关参数
    """

    def __init__(self, appid, env, cluster):
        self.appid = appid
        self.env = env
        self.cluster = cluster

    def __str__(self):
        return f'appid={self.appid} env={self.env} cluster={self.cluster}'


def get_env_clusters(client: httpx.Client, appid):
    """
    获取项目环境与集群
    @param client: http客户端
    @param appid: appid
    @return:
    """
    url = url_get_env_cluster_template.format(appid)
    print(f'获取项目信息：{url}')
    response = client.get(url=url)
    if not response.is_success:
        raise Exception(f'获取Apollo项目信息失败! {response.status_code} {response.text} ')
    return response.json()


def get_configs(client: httpx.Client, apollo: ApolloInfo):
    """
    获取所有配置
    @param client: http客户端
    @param apollo: 相关参数
    @return:
    """
    url = url_get_config_template.format(apollo.appid, apollo.env, apollo.cluster)
    print(f'获取配置信息：{url}')
    response = client.get(url=url)
    if not response.is_success:
        raise Exception(f'获取Apollo配置失败! {response.status_code} {response.text} ')
    return response.json()


def put_configs(client: httpx.Client, apollo: ApolloInfo, namespace, config):
    """
    修改配置
    @param client: http客户端
    @param apollo: 相关参数
    @param namespace: namespace
    @param config: 配置
    @return:
    """
    url = url_put_config_template.format(apollo.appid, apollo.env, apollo.cluster, namespace)
    print(f'修改配置：{url}\n{json.dumps(config, indent=4, ensure_ascii=False)}')
    response = client.put(url=url, json=config)
    if not response.is_success:
        raise Exception(f'修改Apollo配置失败! {response.status_code} {response.text} ')


def init_apollo_info_list(client: httpx.Client) -> List[ApolloInfo]:
    """
    初始化
    @param client: http客户端
    @return: 所有Apollo项目信息
    """
    apollo_info_list = []
    for appid in appid_list:
        entities = get_env_clusters(client, appid)['entities']
        for entity in entities:
            body = entity.get('body')
            env = body.get('env')
            clusters = body.get('clusters')
            for cluster in clusters:
                cluster_name = cluster.get('name')
                apollo_info_list.append(ApolloInfo(appid=appid, env=env, cluster=cluster_name))
    return apollo_info_list


def update_comment(client: httpx.Client, apollo: ApolloInfo):
    """
    更新配置注释
    @param client: http客户端
    @param apollo: 相关参数
    @return:
    """
    nsp_list = get_configs(client=client, apollo=apollo)
    for nsp in nsp_list:
        base_info = nsp.get('baseInfo')
        namespace = base_info.get('namespaceName')
        items = nsp.get('items')
        for item in items:
            config = item.get('item')
            key = config.get('key')
            value = config.get('value')
            comment = config.get('comment')
            if comment != '':
                continue
            if key == '' and value == '':
                continue
            comment = comments.get(key)
            if not comment or comment == '':
                continue
            new_config = {'id': config.get('id'), 'namespaceId': config.get('namespaceId'),
                          'key': key, 'value': value, 'comment': comment}
            try:
                put_configs(client=client, apollo=apollo, namespace=namespace, config=new_config)
            except Exception as e:
                print(f"配置修改失败：{apollo} namespace={namespace} config={new_config} 失败原因：{e}")
            # time.sleep(1)


def run():
    """
    执行入口
    @return:
    """
    with httpx.Client(headers=headers) as client:
        apollo_info_list = init_apollo_info_list(client)
        for apollo_info in apollo_info_list:
            print(apollo_info)
            update_comment(client, apollo_info)


if __name__ == '__main__':
    run()
    print('程序运行完成')
