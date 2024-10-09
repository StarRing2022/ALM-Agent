from apscheduler.schedulers.blocking import BlockingScheduler
import memshort
import memlong
 
def task():
    memshort.gen_short_memory()

    output_file_path = memlong.sortknowledge()
    memlong.sortknowledge_learn(output_file_path)

    # answer = memlong.ltm_answer("什么是心动信号")
    # print(answer)

    print("学习任务已执行...")

def schestart():
    scheduler = BlockingScheduler()
    scheduler.add_job(task, 'interval', seconds=300)
 
    scheduler.start()


if __name__ == "__main__":
    task()
    schestart()