import sqlite3

# Create a connection to the database
connection = sqlite3.connect('data.db') 
cursor = connection.cursor() # cursor is used to interact with the database and execute SQL commands
cursor.execute('CREATE TABLE IF NOT EXISTS videos (title TEXT, duration TEXT)')

def view_videos():
    cursor.execute('SELECT * FROM videos') 
    videos = cursor.fetchall() 
    for index, video in enumerate(videos, start=1):
        print(f'{index}. {video[0]} - {video[1]}')
    return videos    

def add_video():
    title = input('Enter video title: ')
    duration = input('Enter video duration: ')
    add_query = 'INSERT INTO videos VALUES (?, ?)'
    cursor.execute(add_query, (title, duration))
    connection.commit() # commit the changes to the database 
    return view_videos()

def update_video():
    
    video_number = int(input('Enter video number: '))
    title = input('Enter new video title: ')
    duration = input('Enter new video duration: ')
    
    cursor.execute('UPDATE videos SET title = ?, duration = ? WHERE rowid = ?', (title, duration, video_number)) 
    connection.commit()
    return view_videos()

def delete_video():
    try:
        video_number = int(input('Enter video number: '))
    except ValueError:
        print('Invalid input. Please enter a valid integer.')
        return
    cursor.execute('DELETE FROM videos WHERE rowid = ?', (video_number,)) 
    connection.commit() # commit the changes to the database
    return view_videos()

print('***Youtube Manager***')
print('1. List all videos')
print('2. Add video')
print('3. Update video')
print('4. Delete video')
print('5. Exit')

match input('Enter your choice: '):
    case '1':
        view_videos()
    case '2':
        add_video()
    case '3':
        update_video()
    case '4':
        delete_video()
    case '5':
        print('Exiting')
    case _:
        print('Invalid choice')