use std::error::Error;
use std::path::Path;

use nix::sys::stat::lstat;
use nix::sys::stat::Mode;
use nix::sys::stat::SFlag;
use users::get_user_by_uid;
use users::User;
use users::get_group_by_gid;
use users::Group;
use std::fs;
use std::time::SystemTime;
use chrono::Local;
use chrono::DateTime;

pub struct FileStat {
    mode: u32,
    nlink: u64,
    user: User,
    group: Group,
    size: i64,
    modified: SystemTime,
}

impl FileStat {
    pub fn new(path: &Path) -> Result<FileStat, Box<Error>> {
        let stat = lstat(path)?;
        let user = get_user_by_uid(stat.st_uid).ok_or("invalid uid")?;
        let group = get_group_by_gid(stat.st_gid).ok_or("invalid gid")?;

        let modified = fs::metadata(path)?.modified()?;

        Ok(FileStat {
            mode: stat.st_mode,
            nlink: stat.st_nlink,
            user,
            group,
            size: stat.st_size,
            modified,
        })
    }

    pub fn print(&self) {

        let mode_str: String = {
            let mut chars = vec!['-'; 10];
            let flag = SFlag::from_bits_truncate(self.mode);
            let mode = Mode::from_bits_truncate(self.mode);
            if flag.contains(SFlag::S_IFDIR) { chars[0] = 'd'; }
            if mode.contains(Mode::S_IRUSR) { chars[1] = 'r'; }
            if mode.contains(Mode::S_IWUSR) { chars[2] = 'w'; }
            if mode.contains(Mode::S_IXUSR) { chars[3] = 'x'; }
            if mode.contains(Mode::S_IRGRP) { chars[4] = 'r'; }
            if mode.contains(Mode::S_IWGRP) { chars[5] = 'w'; }
            if mode.contains(Mode::S_IXGRP) { chars[6] = 'x'; }
            if mode.contains(Mode::S_IROTH) { chars[7] = 'r'; }
            if mode.contains(Mode::S_IWOTH) { chars[8] = 'w'; }
            if mode.contains(Mode::S_IXOTH) { chars[9] = 'x'; }
            chars.into_iter().collect()
        };

        print!("{} ", mode_str);
        print!("{:>4} ", self.nlink);
        print!("{} ", self.user.name().to_string_lossy());
        print!("{} ", self.group.name().to_string_lossy());
        print!("{:>8} ", self.size);

        let dt: DateTime<Local> = self.modified.into();

        print!("{} ", dt.format("%d/%m/%Y %T"));
    }
}