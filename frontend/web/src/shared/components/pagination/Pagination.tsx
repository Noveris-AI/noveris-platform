import React from "react";
import { Pagination as AntPagination } from "antd";

interface PaginationProps {
  current: number;
  pageSize: number;
  total: number;
  onChange: (page: number, pageSize: number) => void;
}

export const Pagination: React.FC<PaginationProps> = ({
  current,
  pageSize,
  total,
  onChange,
}) => {
  return (
    <AntPagination
      current={current}
      pageSize={pageSize}
      total={total}
      onChange={onChange}
      showSizeChanger
    />
  );
};
