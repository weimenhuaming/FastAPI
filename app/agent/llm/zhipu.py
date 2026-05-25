from zai import ZhipuAiClient

# Initialize client
client = ZhipuAiClient(api_key="aec6ba32d6464b329efd63cff837feb3.W0eFMQFiJD0S25ge")

# Create chat completion
def zhipu(question: str) -> str:  # 或者使用具体的响应类型
    """
    调用智谱AI接口
    
    Args:
        question: 用户问题
        
    Returns:
        包含 choices 的响应对象
    """
    response = client.chat.completions.create(
        model="glm-4-plus",
        messages=[
            {
                "role": "user", 
                "content": question
            }
        ]
    )
    return response.choices[0].message.content

