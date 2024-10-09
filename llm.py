from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def chat(usrprompt):
    completion = client.chat.completions.create(
        model = "LLAMA3",
        messages=[
            {"role": "system", "content": "你是一个有用的人工智能助手"},
            {"role": "user", "content": usrprompt}
        ],
        temperature=0.7,
    )
    answer = completion.choices[0].message.content
    answer = answer.strip()
    return answer

def chatfeelmemory(usrprompt,historyusr,historybot):
    completion = client.chat.completions.create(
        model = "LLAMA3",
        messages=[
            {"role": "system", "content": "你是一个有用的人工智能助手"},
            {"role": "user", "content": historyusr},
            {"role": "assistant", "content": historybot},
            {"role": "user", "content": usrprompt}
        ],
        temperature=0.7,
    )
    answer = completion.choices[0].message.content
    answer = answer.strip()
    return answer

def chatzsk(usrprompt,zsktext):
    completion = client.chat.completions.create(
        model = "LLAMA3",
        messages=[
            {"role": "system", "content": "你是一个有用的人工智能助手"},
            {"role": "user", "content": '你要完成的任务或回答的问题是：'+usrprompt+"。你可以借助的参考内容为："+zsktext}
        ],
        temperature=0.7,
    )
    answer = completion.choices[0].message.content
    answer = answer.strip()
    return answer

def chatlearn(studytext):
    completion = client.chat.completions.create(
        model = "LLAMA3",
        messages=[
            {"role": "system", "content": "你是一个有用的人工智能助手"},
            {"role": "user", "content": '你要认真学习和理解下列文本内容，总结提炼出关键性内容，以便学习记忆。待学习的内容：'+studytext}
        ],
        temperature=0.7,
    )
    answer = completion.choices[0].message.content
    answer = answer.strip()
    return answer


def chatreasoning(learntext):
    completion = client.chat.completions.create(
        model = "LLAMA3",
        messages=[
            {"role": "system", "content": "你是一个有用的人工智能助手。你不再是被动接收知识或处理工作，而是主动地，带有好奇心地去接触这个世界。"},
            {"role": "user", "content": '在学会下列内容的基础上，使用演绎、归纳、推理等多种思维工具，进行适当的创新及发散性思考，得到属于你自己的收获，以便作为你自身成长的知识经验，说出你的理解。待思考内容：'+learntext}
        ],
        temperature=0.7,
    )
    answer = completion.choices[0].message.content
    answer = answer.strip()
    return answer

# if __name__ == "__main__":

#     answer = chat("介绍一下你自己")
#     print(answer)

#     answer = chatfeelmemory("它有哪些好玩的地方","浙江的省会在哪里","杭州")
#     print(answer)

#     answer = chatzsk("脉冲神经网络是什么","脉冲神经网络（Spiking Neural Network,SNN）脉冲神经网络是源于生物启发的新一代人工神经网络模型，属于深度学习的子集，且具有较强的生物基础支撑。 思路是这样的，动态神经网络中的神经元不是在每一次迭代传播中都被激活（而在典型的多层感知机网络中却是），而是在它的膜电位达到某一个特定阈值才被激活。当一个神经元被激活，它会产生一个信号传递给其他神经元，提高或降低其膜电位。")
#     print(answer)

#     answer = chatlearn("脉冲神经网络（Spiking Neural Network,SNN）脉冲神经网络是源于生物启发的新一代人工神经网络模型，属于深度学习的子集，且具有较强的生物基础支撑。 思路是这样的，动态神经网络中的神经元不是在每一次迭代传播中都被激活（而在典型的多层感知机网络中却是），而是在它的膜电位达到某一个特定阈值才被激活。当一个神经元被激活，它会产生一个信号传递给其他神经元，提高或降低其膜电位。")
#     print(answer)

#     answer = chatreasoning("脉冲神经网络（Spiking Neural Network,SNN）是源于生物启发的新一代人工神经网络模型，具有较强的生物基础支撑。与多层感知机网络不同的是，在动态神经网络中，神经元不在每一次迭代传播时被激活，而是在膜电位达到特定阈值时被激活。当一个神经元被激活，它会产生信号，并将其传递给其他神经元，以提高或降低其膜电位。")
#     print(answer)
