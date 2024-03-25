import pandas as pd

def load_state(self, batch_size) -> dict(int, List):
        file: pd.DataFrame = pd.read_csv(
            self.path
        )
        file_size: int = len(file['number'])
        if self.last_read_id < file_size:
            upper_limit: int = self.last_read_id + batch_size

            if upper_limit >= file_size:
                upper_limit = file_size
                batch: List = list(
                    file['number'][self.last_read_id:]
                )
                return batch
            else:
                batch: List = list(
                    file['number'][self.last_read_id:upper_limit]
                )
                return batch

        return None