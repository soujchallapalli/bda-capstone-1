from library import download_video, read_video_urls, write_to_file
import time
from multiprocessing import Pool

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"
    # download_video(url)
    csv_path = "data/video_urls.csv"
    url_list = read_video_urls(csv_path)
    reports_file_path = "reports/sequential_report.md"
    total_download_time = 0
    print(url_list)
    # for url in url_list:
    #     start = time.perf_counter()
    #     download_video(url)
    #     end = time.perf_counter()
    #     elapsed = end - start
    #     serial_time = round(elapsed, 2)
    #     print(f"Serial execution: {serial_time}")
    #     write_to_file(reports_file_path, f"Serial execution: {serial_time}\n")
    #     total_download_time += serial_time
    # print(f"Total download time: {total_download_time}")
    # write_to_file(reports_file_path, f"Total time: {total_download_time}\n")
    
    with Pool() as pool:
        start = time.perf_counter()
        results = pool.map(download_video, url_list)
        end = time.perf_counter()
        elapsed = end - start
        parallel_time = round(elapsed, 2)
        print(f"Parallel execution: {parallel_time}")
    